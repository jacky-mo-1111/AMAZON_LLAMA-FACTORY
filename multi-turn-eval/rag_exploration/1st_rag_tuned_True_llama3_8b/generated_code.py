try:
    with open('example.txt', 'r') as f:
        data = f.read()
except:
    print("Error reading file!")

try {
    const file = new XMLHttpRequest();
    file.open('GET', 'example.txt', true);
    file.send();
} catch (e) {
    console.log('Error reading file!');
}

begin
  File.open('example.txt', 'r') do |f|
    data = f.read
  end
rescue
  puts "Error reading file!"
end

import os

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found!")

def main():
    filename = input("Enter a file name: ")
    print(read_file(filename))

if __name__ == "__main__":
    main()