A balanced delimiter starts with an opening character ((, [, {), ends with a matching
closing character (), ], } respectively), and has only other matching delimiters in between.
A balanced delimiter may contain any number of balanced delimiters.
Examples
The following are examples of balanced delimiter strings:
()[]{}
([{}])
([]{})
The following are examples of invalid strings:
([)]
([]
[])
([})
Input is provided as a single string. Your output should be True or False according to
whether the string is balanced. For example:
Input:
([{}])
Output:
True
def is_balanced(delimiters):
 stack = []
 for char in delimiters:
 if char in "([{":
 stack.append(char)
 elif char in ")]}":
 if not stack:
 return False
 if (char == ")" and stack[-1] == "(") or \
 (char == "]" and stack[-1] == "[") or \
 (char == "}" and stack[-1] == "{"):
 stack.pop()
 else:
 return False
 return not stack
print(is_balanced("()[]{}")) # True
print(is_balanced("([{}])")) # True
print(is_balanced("([]{})")) # True
print(is_balanced("([)]")) # False
print(is_balanced("([{}]")) # False
print(is_balanced("[]{}[")) # False