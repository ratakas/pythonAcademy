from app.Parameter import Parameter
from app.site import site
def main():

    #parametros app
    parameter= Parameter()
    args = parameter.get_agurments()

    site= site(args)  
    siteArg=site.loadArgs()
    site.site_parse()


    
if __name__ == "__main__":
    main()