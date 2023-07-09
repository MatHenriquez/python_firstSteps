# Tipos de datos en Python

# Strings
print("Hello, World!");
print('Hello, World!');
print('''Hello, World!''');
print("""Hello, World!""");

print(type("Hello, World!")); #Expected output <class 'str'>

# Concatenación de strings
print("Hello," + " World!");

# Numbers
print(30); # Int
print(30.5); # Float

print(type(30.5)); #Expected output <class 'float'>

# Boolean
print(True);
print(False);

print(type(True)); #Expected output <class 'bool'>

# list
print([10, 20, 30, 40, 50]);
print(["Hello", "Goodbye", "How are you?"]);

print(type([1, 2, 3])); #Expected output <class 'list'>

# Tuples (listas que No cambian)
print((10, 20, 30)); 

print(type(())); #Expected output <class 'tuple'>

# Diccionarios
print({
    "name": "Ryan", #key-value
    "lastname": "Reynolds",
    "nickname": "RR"
});

print(type({})); #Expected output <class 'dict'>