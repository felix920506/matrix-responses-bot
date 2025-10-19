# Matrix Responses Bot

Matrix responses bot that loads responses from files.

## Basic functionality
The responses folder will contain responses. The responses are markdown (.md) files and jpeg (.jpg) images.
The file extension MUST be lower case on a case sensitive filesystem.

When a command is recieved from one of the channels the bot is in in the format of `{prefix} {message}`, the bot will see if `{message}.md` exists in the responses folder and send it as text in chat. It will then check if `{message}.jpg` exists and send it as an attachment in chat.

## Placeholders
You can have placeholders in the form of `{0}`, `{1}` etc. in the responses markdown files.
When a command is ran with more parameters, it will go like this: `{prefix} {message} {0} {1} {2}...`
The values of `{0}` etc. will be replaced with the command parameters

example:
`placeholder.md` contains the following:
```md
Do {0} then do {1} 
```
Command `{prefix} placeholder something that` will result in message: `Do something then do that`

## Alias support
Put a text file with one line of text in the responses folder with `.alias` extension

Example Alias:
let's say `test.alias` contains the following:
```txt
something
```
the result of `{prefix} test` will be the same as `{prefix} something`
