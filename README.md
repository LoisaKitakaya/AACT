# AACT (AI Application CLI Toolkit) 

## About 

This is a simple program that offers programmers some tools to use to make their development work easier.

It is written in python and is powered by GPT-3 engine.

## Want to run this on your own machine?

### Requirements

To be able to run this program successfully, you need to have the following dependencies installed:

- python3 (obviously)
- python3-venv
- python3-pip

Also you need to have an **OpenAI API Key**. If you don't have it, do this:

- Go [here](https://beta.openai.com/signup) to create an OpenAI account (if you already don't have an account).
- Go [here](https://platform.openai.com/account/api-keys) to generate a new API key.

*Remember to copy your generated API Key somewhere safe.*

### Installation Instructions

To install this program to your local system, follow these instructions.

```
# clone this repo
$ git clone https://github.com/LoisaKitakaya/AACT.git

# move into cloned directory
$ cd AACT

# run 'install.sh' file using:
$ ./install.sh
# or
$ bash install.sh
```

To be able to successfully make calls to the OpenAI API, you need to provide the program with your API key. To do so, copy this command to your terminal.

```
# replace 'example key' with your API key
$ echo "OPENAI_API_KEY='example key'" > ~/.AACT/.env
```

That should do it.

**NOTE:** Make sure to carefully follow the instructions that will be provided during installation.

## Issues

If you encounter any problems with the code or otherwise, please submit an issue [here](https://github.com/LoisaKitakaya/AACT/issues).

## Contributing

If you wanna contribute to the project, feel free to do so. Just clone the repository and submit a pull request, we can do some cool stuff with this API 😌.

## License

#### The MIT License (MIT)

Copyright © 2023 Freedom Loisa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.