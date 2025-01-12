```
 _______    ______   __       __                                      __                     
|       \  /      \ |  \  _  |  \                                    |  \                    
| $$$$$$$\|  $$$$$$\| $$ / \ | $$  _______   ______    ______    ____| $$  ______    ______  
| $$__| $$| $$__| $$| $$/  $\| $$ /       \ /      \  /      \  /      $$ /      \  /      \ 
| $$    $$| $$    $$| $$  $$$\ $$|  $$$$$$$|  $$$$$$\|  $$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$\
| $$$$$$$\| $$$$$$$$| $$ $$\$$\$$| $$      | $$  | $$| $$   \$$| $$  | $$| $$    $$| $$   \$$
| $$  | $$| $$  | $$| $$$$  \$$$$| $$_____ | $$__/ $$| $$      | $$__| $$| $$$$$$$$| $$      
| $$  | $$| $$  | $$| $$$    \$$$ \$$     \ \$$    $$| $$       \$$    $$ \$$     \| $$      
 \$$   \$$ \$$   \$$ \$$      \$$  \$$$$$$$  \$$$$$$  \$$        \$$$$$$$  \$$$$$$$ \$$      
```

## Setup
Install the `rawcorder` cli with pip inside thi repository.\
For debugging and development purposes you can use `-e` to apply local code changes immediately.
```bash
pip3 install -e .
```

### Environment Variables
To configure the RabbitMQ Message Queue, you have to provide a `.env` file with the following variables:
```
RABBIT_MQ_HOST=
```

## Usage
`rawcorder` enables you to capture all messages of a RabbitMQ Queue in order to replay them afterwards.

### `rawcorder record`
To record queue data into a file, you can use the `record` command.
```
Usage: rawcorder record [OPTIONS]

  Record Queue Data to a file.

  Author:     Benedikt SCHWERING <mail@bschwer.ing>

Options:
  -o, --output FILE  [required]
  -a, --append
  --help             Show this message and exit.
```

### `rawcorder replay`
To replay queue data from a file, you can use the `replay` command.
```
Usage: rawcorder replay [OPTIONS]

  Replay Queue Data from a file.

  Author:     Benedikt SCHWERING <mail@bschwer.ing>

Options:
  -i, --input FILE     [required]
  -d, --delay INTEGER  [default: 500]
  --help               Show this message and exit.
```
