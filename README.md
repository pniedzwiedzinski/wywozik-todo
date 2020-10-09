# wywozik-todo

Add to your todoist list task that will remind you to take out trash. This works
by getting data from https://wywozik.pl

## NixOS

Add [NUR](https://github.com/nix-community/NUR) and you will be able to use wywozik-todo from nix

```nix
{pkgs}:
let
  wywozik = pkgs.nur.repos.pn.wywozik-todo.override {
    configFile = ''
      CITY = "Poznań"
      STREET = "ul. Święty Marcin"
      NUMBER = "1"
      HOUSING = "zamieszkana"
      TOKEN = "token"
    '';
  };
in
{...}
```

## Running in docker

1. Setup `config.py` file (see `config.def.py`)
2. `docker run -it --name wywozik -v $(pwd)/config.py:/app/config.py pniedzwiedzinski/wywozik`
3. Now you can run it with `docker start wywozik`

## Running manually

1. Setup `config.py` file (follow `config.def.py`)
2. `pip3 install requirements`
3. `python3 main.py` - you can setup cron job for it to run everyday

## TODO

- [ ] Adding custom label
- [ ] Adding to project
- [ ] Filtering by trash type
- [ ] Get Engineering degree and develop a robot that will take the trash out autonomously
