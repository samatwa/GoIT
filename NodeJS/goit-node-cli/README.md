# Node.js contacts CLI — Viacheslav Kuznetsov

## Assignment 1

Create a contacts CLI using [Commander](https://www.npmjs.com/package/commander), Node.js filesystem promises and a JSON contact collection.

## Setup

From this project directory, install the locked dependencies:

```shell
npm ci
```

The implementation is in [src](./src). `src/contacts.js` imports `fs/promises` and `path`, resolves `contactsPath` to the JSON database and exports asynchronous collection functions.

| Function | Required result |
|---|---|
| `listContacts()` | Array of contacts |
| `getContactById(contactId)` | Matching contact, or null |
| `removeContact(contactId)` | Removed contact, or null |
| `addContact(name, email, phone)` | Newly created contact, including its ID |

Storage functions use `readFile()` and `writeFile()` and return data without printing. `src/index.js` imports them and dispatches actions through `invokeAction()`, which prints the selected operation's result.

## Example commands

Run from the project directory:

```shell
# Display all contacts as a table
node src/index.js -a list

# Display a matching contact, or null
node src/index.js -a get -i 05olLMgyVQdWRwgKfg5J6

# Add and display a contact
node src/index.js -a add -n Mango -e mango@gmail.com -p 322-22-22

# Remove and display a contact, or null
node src/index.js -a remove -i qdggE76Jtbfd9eWJHrssH
```

## Acceptance criteria

The coursework must follow the specification, contain no commented-out implementation blocks, and run on the required Node.js LTS release. The original assignment also required submitting the repository link to a mentor.
