import yaml
import re
import ast

class CrazyTransformer(ast.NodeTransformer):

    """
    A child class of NodeTransformer, this class visit all the node of the loaded ast and when it visit
    a Name node wich has for id a variable present in mytool : it applies visit_Name : it replace the Name
    node by a constant Node containing the corresponding value of the variable:
    example:
     Node : Name(id='kmersize', ctx=Load())
    kmersize exist in mytool.variables and mytool.__getattribute__(kmersize) == 10
    New Node : Constant(value=10, kind=None)
    """
    def __init__(self):
        self.yolo = None

    def visit_Name(self, node, bite=None):
        if node.id in self.yolo.variables:
            node = ast.Constant(value=self.yolo.__getattribute__(node.id), kind=None)
        return node

class mytool:
    """
    mytool is a class that is linked to the tools.yaml file and used to extract informations from it and make
    calcul with it
    """
    def __init__(self,tool_name):
        """
        :param tool_name: a string containing the exact ( exact for the moment will use re)
        """
        self.tool_name=tool_name
        self.dict = self.find_da_tool()
        if type(self.dict) == str:
            print(self.dict)
            quit
        else:
            self.variables = self.dict["variables"]
            for element in self.variables:
                self.__setattr__(element[1:],None)
            print("please add the different variables needed : " , self.variables , "\n with the following syntax : " )
            print("mytool.variable = float or mytool.variable = int" ,)

    def find_da_tool(self):
        """
        this function navigate through tools.yaml to find the dictionnary which has the same name as sel.tool_name
        if it finds it, it return the corresponding dictionnary
        if not it returns a string  \ tool not finded /
        :return: dictionnary
        """
        with open("tools.yaml") as tools_file:
            tools_dict = yaml.load(tools_file)
            for key in tools_dict:
                if self.tool_name == key[1:]:
                    return tools_dict[key]
            return "tool not finded"

    def check_variables(self):
        """
        check if all the variables was inputed by the user
        :return:
        """
        for element in self.variables:
            try:
                self.__getattribute__(element)
            except:
                return "CONSIDER ADDING ALL THE VARIABLES NEEDED !!!!"
        return True


    def time_complexity(self):
        if self.check_variables() == True:
            tree = ast.parse(self.dict["time_complexity"],mode='eval')
            dict_tree = ast.dump(tree)
            parser = CrazyTransformer()
            #put all the mytool class into yolo object of parser (DUUMB)
            parser.yolo  = self
            tree = parser.visit(tree)
            #expr_tree = ast.Expression(body=tree)
            ast.fix_missing_locations(tree)
            compiled_new_expr = compile(tree,filename='',mode='eval')
            print(eval(compiled_new_expr))
            return eval(compiled_new_expr)
        else:
            return("ADD ALL VARIABLES")


    def memory_complexity(self):
        if self.check_variables() == True:
            tree = ast.parse(self.dict["memory_complexity"],mode='eval')
            dict_tree = ast.dump(tree)
            parser = CrazyTransformer()
            #put all the mytool class into yolo object of parser (DUUMB)
            parser.yolo  = self
            tree = parser.visit(tree)
            #expr_tree = ast.Expression(body=tree)
            ast.fix_missing_locations(tree)
            compiled_new_expr = compile(tree,filename='',mode='eval')
            print(eval(compiled_new_expr))
            return eval(compiled_new_expr)
        else:
            return("ADD ALL VARIABLES")

