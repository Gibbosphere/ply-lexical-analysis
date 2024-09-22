import ply.lex as lex
import sys

# List of token names
tokens = (
    'WORD',
    'NUMBER',
    'WHITESPACE',
    'PUNCTUATION',
    'HASHTAG',
    'NAME',
    'ILLEGAL'
)

# Functions defining token regular expressions and formatting tokens
def t_WORD(t):
    r'[a-zA-Z]+'  # Regular expression
    t.value = f'WORD,{t.value}'  # Format the tokens
    return t

def t_ILLEGAL(t):
    r'[^a-zA-Z0-9 \t.,;!?#@]'
    t.value = f'ILLEGAL,{t.value}'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = f'NUMBER,{t.value}'
    return t

def t_WHITESPACE(t):
    r'[ \t]+'
    t.value = f'WHITESPACE,{t.value}'
    return t

def t_PUNCTUATION(t):
    r'[.,;!?]'
    t.value = f'PUNCTUATION,{t.value}'
    return t

def t_HASHTAG(t):
    r'\#[a-zA-Z0-9]+'
    t.value = f'HASHTAG,{t.value}'
    return t

def t_NAME(t):
    r'\@[a-zA-Z]+'
    t.value = f'NAME,{t.value}'
    return t

# Handling an error rule
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Tokenize all the file content using previous token functions
def tokenize_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()

        lexer.input(data)

        # Output to .tkn file
        output_filename = filename.replace('.msg', '.tkn')
        with open(output_filename, 'w') as token_file:
            for tok in lexer:
                print(tok.value)  # Print token to the console
                token_file.write(tok.value + '\n')  # Write token to the file

    except FileNotFoundError:
        print(f"The file '{filename}', does not exist.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage of this program: lex_msg.py <inputfile.msg>")
    else:
        tokenize_file(sys.argv[1])

