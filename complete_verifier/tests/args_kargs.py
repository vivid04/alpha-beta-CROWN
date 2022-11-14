

h = ["general"]

def args_kwargs(*args, **kwargs):

     """Add a single parameter to the parser. We will check the 'hierarchy' specified and then pass the remaining arguments to argparse.
     args是一个tuple
     kwargs是一个dict
     """
     print(args)
     print(kwargs)
     if 'hierarchy' not in kwargs:
         raise ValueError("please specify the 'hierarchy' parameter when using this function.")
     hierarchy = kwargs.pop('hierarchy')
     help = kwargs.get('help', '')
     private_option = kwargs.pop('private', False)
     # Make sure valid help is given
     if not private_option:
         if len(help.strip()) < 10:
             raise ValueError(f'Help message must not be empty, and must be detailed enough. "{help}" is not good enough.')
         elif (not help[0].isupper()) or help[-1] != '.':
             raise ValueError(f'Help message must start with an upper case letter and end with a dot (.); your message "{help}" is invalid.')
if __name__ == '__main__':
    
    args_kwargs('--pgd_order', choices=["before", "after", "skip"], default="before",  help='Run PGD before/after incomplete verification, or skip it.', hierarchy=h + ["pgd_order"])