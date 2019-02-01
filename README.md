# state
Experiment in state management for workflow systems (Galaxy, CWL)

## Usage

Define your initial state as a json file:

```
{
  "x": 0,
  "y": 0
}
```
Define your update functions as python lambda functions:

```
{
    "x": "lambda x: x + 1",
    "hello": "lambda x: 'world'"
}
```

The functions will be applied by passing the initial state into the update function. If the key doesn't exist, it will be added

```
state.py initial_state.json updates.json
{
  "x": 1, 
  "y": 0, 
  "hello": "world"
}
```
