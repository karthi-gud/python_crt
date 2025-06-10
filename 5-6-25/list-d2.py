Prog_lang=['c', 'c++', 'java', 'python', 'javascript']
print(Prog_lang)
front_end = ['html', 'css', 'javascript']
print(front_end)
Prog_lang.extend(front_end)
print(Prog_lang)  # ['c', 'c++', 'java', 'python', 'javascript', 'html', 'css', 'javascript']
print(Prog_lang.count('javascript'))  # 2
print(Prog_lang.index('python'))  # 3
Prog_lang.insert(2, 'ruby')
print(Prog_lang)  # ['c', 'c++', 'ruby', 'java', 'python', 'javascript', 'html', 'css', 'javascript']
Prog_lang.remove('c++')
print(Prog_lang)  # ['c', 'ruby', 'java', 'python', 'javascript', 'html', 'css', 'javascript']
Prog_lang.pop(3)
print(Prog_lang)  # ['c', 'ruby', 'java', 'javascript', 'html', 'css', 'javascript']
Prog_lang.clear()
print(Prog_lang)  # []
Prog_lang = ['c', 'c++', 'java', 'python', 'javascript']
Prog_lang.reverse()
print(Prog_lang)  # ['javascript', 'python', 'java', 'c++', 'c']
Prog_lang.sort()
print(Prog_lang)  # ['c', 'c++', 'java', 'javascript', 'python']
Prog_lang = ['c', 'c++', 'java', 'python', 'javascript']
Prog_lang_copy = Prog_lang.copy()
print(Prog_lang_copy)  # ['c', 'c++', 'java', 'python', 'javascript']
Prog_lang.append('ruby')
print(Prog_lang)  # ['c', 'c++', 'java', 'python', 'javascript', 'ruby']
Prog_lang.extend(['html', 'css'])
print(Prog_lang)  # ['c', 'c++', 'java', 'python', 'javascript', 'ruby', 'html', 'css']
Prog_lang.insert(1, 'go')
print(Prog_lang)  # ['c', 'go', 'c++', 'java', 'python', 'javascript', 'ruby', 'html', 'css']
Prog_lang.remove('javascript')
print(Prog_lang)  # ['c', 'go', 'c++', 'java', 'python', 'ruby', 'html', 'css']