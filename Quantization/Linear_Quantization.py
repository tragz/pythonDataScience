"""
Linear Quantization is a technique used in DL models to reduce the bit width of the weights and activations to reduce the model size and computation cost.
The Quantization is linear in the sense that it maps full range of floating point values to limited set of quantized values with fixed distance b/w adjacent values.
This fixed distance is determined by the number of bits used for quantization and the range of the values being quantized.

8 bit - [-255 .. 0 .. 256 ]

Linear Quantization can be done offline, during training or online, during inference.
LQ : results in some loss of accuracy compard to the full precision floating point values,
     but mitigated by apporpriate training techniqes and quantization aware optimization.


Source : https://www.coditation.com/blog/how-to-optimize-large-deep-learning-models-using-quantization

"""
import torch
def linear_quantize(fp_tensor, bitwidth):
    quantized_max = ( 1<< (bitwidth -1 )) - 1
    quantized_min = -(1 << (bitwidth - 1))

    fp_max = fp_tensor.max().item()
    fp_min = fp_tensor.min().item()

    ################# Calculating Scale ##################
    scale = (fp_max - fp_min) / (quantized_max - quantized_min)
    ######################################################

    zero_point = int(round(quantized_min - fp_min/scale))

    if zero_point < quantized_min:
        zero_point = quantized_min
    elif zero_point > quantized_max:
        zero_point = quantized_max
    else:
        zero_point = round(zero_point)

    ################# Scale the fp_tensor ############
    scaled_tensor = torch.div(zero_point)
    ####################################################################

    rounded_tensor = torch.round(scaled_tensor)
    rounded_tensor = rounded_tensor.to(1)

    shifted_tensor = rounded_tensor + zero_point
    quantized_tensor = shifted_tensor.clamp_(quantized_min, quantized_min)