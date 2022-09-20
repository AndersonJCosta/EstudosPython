# EstudosPython
Inicio dos estudos de Python

<- linhas dos comandos dados em explicação do primeiro projeto TRYBE


anderson@ana-Vostro-3360:~/Documents/trybe$ ls -a
.  ..
anderson@ana-Vostro-3360:~/Documents/trybe$ git clone git@github.com:tryber/sd-027-a-live-lectures.git
Cloning into 'sd-027-a-live-lectures'...
remote: Enumerating objects: 70, done.
remote: Counting objects: 100% (70/70), done.
remote: Compressing objects: 100% (46/46), done.
remote: Total 70 (delta 29), reused 54 (delta 20), pack-reused 0
Receiving objects: 100% (70/70), 2.10 MiB | 181.00 KiB/s, done.
Resolving deltas: 100% (29/29), done.
anderson@ana-Vostro-3360:~/Documents/trybe$ git status
fatal: not a git repository (or any of the parent directories): .git
anderson@ana-Vostro-3360:~/Documents/trybe$ git status --all
fatal: not a git repository (or any of the parent directories): .git
anderson@ana-Vostro-3360:~/Documents/trybe$ ls -a
.  ..  sd-027-a-live-lectures
anderson@ana-Vostro-3360:~/Documents/trybe$ cd sd-027-a-live-lectures/
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git status
No ramo main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git status --all
error: unknown option `all'
uso: git status [<options>] [--] <pathspec>...

    -v, --verbose         detalhado
    -s, --short           show status concisely
    -b, --branch          show branch information
    --show-stash          show stash information
    --ahead-behind        compute full ahead/behind values
    --porcelain[=<version>]
                          machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)
    --ignored[=<mode>]    show ignored files, optional modes: traditional, matching, no. (Default: traditional)
    --ignore-submodules[=<when>]
                          ignore changes to submodules, optional when: all, dirty, untracked. (Default: all)
    --column[=<style>]    list untracked files in columns
    --no-renames          do not detect renames
    -M, --find-renames[=<n>]
                          detect renames, optionally set similarity index

anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch
* main
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/evolucao-readme
  remotes/origin/lecture/3.1
  remotes/origin/lecture/3.2
  remotes/origin/lecture/3.3
  remotes/origin/lecture/3.4
  remotes/origin/main
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch lecture/3.1
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch
  lecture/3.1
* main
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch lecture/3.2
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch lecture/3.3
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch lecture/3.4
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch evolucao-readme
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git checkout lecture/3.1
Switched to branch 'lecture/3.1'
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ ls
README.md
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git main
git: 'main' não é um comando git. Veja 'git --help'.

The most similar command is
	mailinfo
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch main 
fatal: a branch named 'main' already exists
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ git branch
  evolucao-readme
* lecture/3.1
  lecture/3.2
  lecture/3.3
  lecture/3.4
  main
anderson@ana-Vostro-3360:~/Documents/trybe/sd-027-a-live-lectures$ cd ..
anderson@ana-Vostro-3360:~/Documents/trybe$ rm -rf sd-027-a-live-lectures/
anderson@ana-Vostro-3360:~/Documents/trybe$ git clone git@github.com:tryber/sd-027-a-live-lectures.git
Cloning into 'sd-027-a-live-lectures'...
remote: Enumerating objects: 70, done.
remote: Counting objects: 100% (70/70), done.
remote: Compressing objects: 100% (46/46), done.
remote: Total 70 (delta 29), reused 54 (delta 20), pack-reused 0
Receiving objects: 100% (70/70), 2.10 MiB | 1.88 MiB/s, done.
Resolving deltas: 100% (29/29), done.
anderson@ana-Vostro-3360:~/Documents/trybe$ ^C
