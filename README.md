# SubConv-sing-box

This is a subscription converter for sing-box.

**Note: This project is still under development. There may be bugs and breaking changes.**

**Issues and PRs are welcome.**

## Todo

- [x] parse nodes from sing-box config
- [ ] parse nodes from mihomo config
- [ ] parse nodes from share link
- [ ] rewrite the web ui (**the current one is literally copied from [SubConv](https://github.com/SubConv/SubConv)**)

## Development Guide

### Dependencies

- Python 3

```shell
pip install -r requirements.txt
```

### File Structure

```shell
.
├── config/          # used to parse config for this project
├── generate/        # used to generate sing-box config
├── parse/           # used to parse nodes from inputs (like sing-box config, mihomo config, share link, etc.)
├── type/            # classes used to compose the sing-box config
├── mainpage/        # source code of the web ui
├── static/          # static files of the web ui (compiled from mainpage/)
├── main.py          # entry point of the project
├── README.md        # this file
└── requirements.txt # dependencies
```

### Run

Run `python main.py --help` for help.

