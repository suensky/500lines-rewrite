# code = "print('Hello ' + name)"
code = """
_output_.append('Hello, ')
_output_.append(str(name))
_output_.append('!')
"""
output = []
ctx = {"name": "user", "_output_": output}
code = compile(code, '', 'exec')
exec(code, None, ctx)
print(output)
print("".join(output))