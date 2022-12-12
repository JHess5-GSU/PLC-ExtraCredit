import re               # Thank God for regular expressions
import sys

class Tokenize():
    def __init__(self, infile):
        self.my_code = open(infile, 'r')

    def run(self, outfile):

        ERROR_FUSE = False      # Blow this fuse on errors so we know, but keep going.
        ERROR_LINE = 0          

        lex_tok_list = []       # Stores my lex's and my tok's.   [["Lex","Token"],...]

        var_regex = re.compile("^(([A-Za-z]*[_]*)+)$")
        # Match any combo of letters and underscores. Will check length first below.

        num_regex = re.compile("^(\d+)$")
        # Match any amount of digits.

        real_regex = re.compile("^(\d+.\d+)$")
        # Match any amount of digits that also contain one ‘.’

        comm_regex = re.compile("^(##+)$")
        # Match two or more “#” to be a comment start

        for line in self.my_code:    # Go through all lines of source code

            ERROR_LINE += 1     # Today I learned that line counts start at 1, not 0.  
            i = 0
            line = line.replace("\n"," \\n")    # To help me detect newlines.
            string = line.split(' ')        # In this lang, lex's are sep'd by spaces
            last_index = len(string) - 1
            last_str = string[last_index]
            last_str_len = len(last_str)

            while (i+1 <= len(string)):    
                ERROR_FLAG = False

                if (string[i] == '\\n'):
                    pass

                elif (string[i] == '<JASON>'):
                    lex_tok_list.append([string[i],"0"])
                elif (string[i] == '<NOSAJ>'):
                    lex_tok_list.append([string[i],"1"])


                elif (string[i] == ';'):
                    lex_tok_list.append([string[i],"2"])

                elif (string[i] == '+'):
                    lex_tok_list.append([string[i],"3"])
#                elif (string[i] == '++'):
#                    lex_tok_list.append([string[i],"4"])

                elif (string[i] == '-'):
                    lex_tok_list.append([string[i],"5"])
#                elif (string[i] == '--'):
#                   lex_tok_list.append([string[i],"6"])

                elif (string[i] == '*'):
                    lex_tok_list.append([string[i],"7"])
                elif (string[i] == '/'):
                    lex_tok_list.append([string[i],"8"])
                elif (string[i] == '%'):
                    lex_tok_list.append([string[i],"9"])

                elif (string[i] == '<'):
                    lex_tok_list.append([string[i],"10"])
                elif (string[i] == '>'):
                    lex_tok_list.append([string[i],"11"])
                elif (string[i] == '<='):
                    lex_tok_list.append([string[i],"12"])
                elif (string[i] == '>='):
                    lex_tok_list.append([string[i],"13"])

                elif (string[i] == '='):
                    lex_tok_list.append([string[i],"14"])
                elif (string[i] == '=='):
                    lex_tok_list.append([string[i],"15"])
                elif (string[i] == '!='):
                    lex_tok_list.append([string[i],"16"])

                elif (string[i] == 'and'):
                    lex_tok_list.append([string[i],"17"])
                elif (string[i] == 'or'):
                    lex_tok_list.append([string[i],"18"])                    
       
                elif (string[i] == '('):
                    lex_tok_list.append([string[i],"19"])                
                elif (string[i] == ')'):
                    lex_tok_list.append([string[i],"20"])

                elif (string[i] == 'if'):
                    lex_tok_list.append([string[i],"21"])                
                elif (string[i] == 'for'):
                    lex_tok_list.append([string[i],"22"])
                elif (string[i] == 'while'):
                    lex_tok_list.append([string[i],"23"])
                elif (string[i] == 'else'):
                    lex_tok_list.append([string[i],"24"])

                elif (string[i] == '{'):
                    lex_tok_list.append([string[i],"25"])
                elif (string[i] == '}'):
                    lex_tok_list.append([string[i],"26"])

                elif (string[i] == 'char'):
                    lex_tok_list.append([string[i],"27"])                
                elif (string[i] == 'int'):
                    lex_tok_list.append([string[i],"28"])
                elif (string[i] == 'real'):
                    lex_tok_list.append([string[i],"29"])
                elif (string[i] == 'bool'):
                    lex_tok_list.append([string[i],"30"])
                elif (string[i] == 'string'):
                    lex_tok_list.append([string[i],"31"])

                elif (num_regex.match(string[i])):
                    lex_tok_list.append([string[i],"32"])

                elif (real_regex.match(string[i])):
                    lex_tok_list.append([string[i],"33"])

                elif (comm_regex.match(string[i])):
                    # Matched ## so skip to end of line.
                    i+=1
                   
                    while (i+1 <= len(string)):
                        i+=1            

                elif (len(string[i]) >= 1 and len(string[i]) <= 64):

                    if (var_regex.match(string[i]) != None):
                        lex_tok_list.append([string[i],"34"])
                    else:
                        #lex_tok_list.append([string[i],"BAD_VAR"])
                        ERROR_FLAG = True

                elif (string[i] == '"'):
                    stringtext = ''
                    if ( i+1 <= len(string) ):
                        i+=1
                        while (string[i] != '"' and i+1 < len(string)):
                            # Searching for end of string.
                            stringtext += str(string[i]) + " "
                            i+=1
                        if ( i+1 > len(string)):
                            ERROR_FLAG = True
                            # No end of string found before EOL
                        else:
                            lex_tok_list.append([stringtext,"35"])

                    else:
                        ERROR_FLAG = True   # No end of string found before EOL
                    # Starting a string.

                elif (string[i] == ","):
                    lex_tok_list.append([string[i],"36"])

                elif (string[i] == "True"):
                    lex_tok_list.append([string[i],"37"])   # Booleans
                
                elif (string[i] == "False"):
                    lex_tok_list.append([string[i],"37"])
                
                elif (string[i] == "class"):
                    lex_tok_list.append([string[i],"38"])
                
                elif (string[i] == "method"):
                    lex_tok_list.append([string[i],"39"])

                elif (string[i] == ''):
                    pass
                

                elif (string[i] == ','):
                    lex_tok_list.append([",","COMMA"])

                else:
                    lex_tok_list.append([string[i],"UNKNOWN"])
                    ERROR_FLAG = True

                if (ERROR_FLAG):
                    print("THERE WAS AN ERROR ON LINE {} - BAD LEXEME WAS: {}" \
                        .format(ERROR_LINE, string[i]))
                    ERROR_FUSE = True

                i+=1

        if (ERROR_FUSE):
            print("No output due to error(s)")
        else:
            self.my_tokens = open(outfile, 'w')
            for x in range(len(lex_tok_list)):
                #print(lex_tok_list[x])
                self.my_tokens.write(str(lex_tok_list[x])+'\n')
               
            self.my_tokens.close()
            print(lex_tok_list)

        self.my_code.close()
       

        print()
        print()



class ParseTokens():

    my_vars = {}
    var_types = {}

    def __init__(self, infile):

        self.index = 0
        self.my_tokens = open(infile, 'r')
        self.lines = self.my_tokens.readlines()

        for x in range(len(self.lines)):
            self.lines[x] = self.lines[x].strip('\'').strip('][\n').split(', ')
           
            for y in range(2):
                self.lines[x][y] = self.lines[x][y].strip('\'')

            #print(self.lines[x])

        self.current_token = self.lines[0][1]
        self.current_lexeme = self.lines[0][0]
        self.current_element = self.lines[0]
       

    def get_next_token(self):
        if (self.index + 1 >= len(self.lines)):
            return None


        self.index += 1
        self.current_element = self.lines[self.index]
        self.current_lexeme = self.lines[self.index][0]
        self.current_token = self.lines[self.index][1]


        return self.current_token
       

    def program(self):
        if self.current_token == '0':
            print("Start found")
            self.get_next_token()
            self.statement_list()

            if self.get_next_token() != '1':
                print("Missing end of program.")
                sys.exit()
            else:
                print("Complete")
                print()

    def statement_list(self):
        if self.current_token == '25':
            #print("Statement start found")
            self.get_next_token()

            while (self.current_token == '21' or self.current_token == '23' or self.current_token == '27' or self.current_token == '28'\
                 or self.current_token == '29' or self.current_token == '30' or self.current_token == '31' or self.current_token == '34'\
                 or self.current_token == '38' or self.current_token == '39'):
                self.statement()

                if (self.get_next_token() != "SC"):
                    self.error()            
                #print("SC Found")
                self.get_next_token()

            if (self.current_token != '26'):
                print("{} Found instead of RCURLY".format(self.current_element))
                self.error()

    def statement(self):
        if (self.current_token == '21'):
            self.if_statement()
        elif (self.current_token == '23'):
            self.while_statement()
        elif (self.current_token == '27'):
            self.declare()
        elif (self.current_token == '28'):
            self.declare()
        elif (self.current_token == '29'):
            self.declare()
        elif (self.current_token == '30'):
            self.declare()
        elif (self.current_token == '31'):
            self.declare()
        elif (self.current_token == '34'):
            self.ass()
        elif (self.current_token == '38'):
            self.aclass()
        elif (self.current_token == '39'):
            self.amethod()

    def aclass(self):
        pass

    def amethod(self):
        pass

    def while_statement(self):
        pass

    def if_statement(self):
        self.get_next_token()

    def var(self):
        pass

    def declare(self):
        if (self.get_next_token() != '34'):
            self.error()
        else:
            #self.lines[self.index][2] = 0
            self.my_vars[self.current_lexeme] = None
            #print(self.my_vars)
            self.var_types[self.current_lexeme] = self.lines[self.index-1][0]
            print("New variable {} of type {}".format(self.current_lexeme, self.var_types[self.current_lexeme]))

    def ass(self):
        # <ass> :  34 = <expr>
        if self.current_token == '34':
            if (self.get_next_token() == '14'):
                self.express()
            else:
                self.error()
        else:
            self.error()
   
    def factor(self):
        #print("Factor Found")
        self.get_next_token()

        if (self.current_token == '34'):
            self.my_vars[self.lines[self.index-2][0]] = self.my_vars[self.current_lexeme]
            print("Assigned {} the value of {}, which was {}".format(self.lines[self.index-2][0], self.current_lexeme, self.my_vars[self.lines[self.index-2][0]]))

        elif (self.current_token == 'NUM'):
            self.my_vars[self.lines[self.index-2][0]] = self.lines[self.index][0]
            print("Assigned {} a value of {}".format(self.lines[self.index-2][0], self.lines[self.index][0]))
            #print(self.my_vars[self.lines[self.index-2][0]])

        elif (self.current_token == '19'):
            self.express()
            if (self.get_next_token() != '20'):
                self.error()
        else:
            self.error()


    def express(self):
        self.term()
        while (self.current_token == '3' or self.current_token == '5'):
            self.get_next_token()
            self.term()    

    def term(self):
        self.factor()
        while (self.current_token == '7' or self.current_token == '8' or self.current_token == '9'):
            self.get_next_token()
            self.term()

    def error(self):
        print("There was an error at {}, line {}. Stopping".format(self.current_element, self.index+1))
        sys.exit()
       
    def run(self):
        self.program()

        self.my_tokens.close()

#Tokenize("testcode.txt", "testtokens.txt").run()
#ParseTokens("testtokens.txt").run()
#ParseTokens("tokens.txt").run()


Tokenize("failWhile.txt").run('failWhileOutput.txt')
#ParseTokens("testtokens1.txt").run()


