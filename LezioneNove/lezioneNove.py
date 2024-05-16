#*args e **kwargs

def nome_funzione(arg_1 : int, **kwargs):

    alpha: float = kwargs["alpha"]

nome_funzione(arg_1=1.0, alpha=5.0) #alpha = key 5.0 = value

########

def complex_statistical_function(x,distrubuition_type, **kwargs):

    if distrubuition_type == "geometric":
        p : float = kwargs["p"]
    
    elif distrubuition_type == "poisson":

        lambda_1: float = kwargs["lambda"]


complex_statistical_function(x=1.0, distrubuition_type="geometric",p=5.0)
complex_statistical_function(x=2.0, distrubuition_type="poisson",lambda_1 = 5.0)