import glob
print(len(dir(glob)))
print(dir(glob))
print(glob.glob('*.py'))
print(glob.glob('**/*.py', recursive=True))
print(glob.glob('*.txt'))
print(glob.glob('Test/processed/*.py'))