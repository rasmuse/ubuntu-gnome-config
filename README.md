# ubuntu-gnome-config

## Using Ubuntu Gnome 15

## Workspace extensions
Install Workspace Grid to get a two-dimensional layout of workspaces.

https://extensions.gnome.org/extension/484/workspace-grid/

Install No Topleft Hot Corner to remove that annoyance.

https://extensions.gnome.org/extension/118/no-topleft-hot-corner/

Install TopIcons extensions to not have legacy tray icons, e.g. Dropbox, take space on the bottom left corner of the screen

https://extensions.gnome.org/extension/495/topicons/


## First round of apt-get

```
sudo apt-get install curl git
```

## Enable hibernate

```
apt-get install hibernate pm-utils
```

(Not sure whether ```pm-utils``` is needed. This is black magic zone.)

Now put some secret configuration in a new file:

```
sudo cp ~/ubuntu-gnome-config/hibernate/com.ubuntu.enable.hibernate.pkla /var/lib/polkit-1/localauthority/50-local.d/
```


## Configure some basics in Firefox

To edit settings, edit the ~/ubuntu-gnome-config/firefox/user.js and run

```
cp ~/ubuntu-gnome-config/firefox/user.js `python3 ~/ubuntu-gnome-config/firefox_default_user.py`
```

(Maybe create a symbolic link instead?)


## Basic dev stuff

```
apt-get install git python-dev python3-dev gfortran
pip install --user vex
```

`.bashrc` settings in `~/ubuntu-gnome-config/bashrc-additions.sh`. Add them:

```
echo '. ~/ubuntu-gnome-config/bashrc-additions.sh' >> ~/.bashrc
```

### Download and install Hack font

http://sourcefoundry.org/hack/

For example, to put in the user ~/.fonts directory

```
HACKFONTURL=https://github.com/chrissimpkins/Hack/releases/download/v2.018/Hack-v2_018-ttf.zip \
sh -c '
mkdir -p ~/.fonts && \
cd ~/.fonts && \
curl -L $HACKFONTURL > hackfont.zip \
&& unzip hackfont.zip \
&& rm hackfont.zip'
```

Open Tweaks and go to Fonts tab to set Monospace to `Hack`. How to do that from the shell?

### Change colors in Gnome Terminal

git clone https://github.com/chriskempson/base16-gnome-terminal.git
./base16-gnome-terminal/base16-monokai.dark.sh 

curl -L https://raw.githubusercontent.com/jtheoof/dotfiles/master/dircolors.monokai > ~/.dircolors

## LaTeX

```
apt-get install texlive texlive-math-extra texlive-bibtex-extra latexmk xzdec biber

tlmgr init-usertree
tlmgr install mathdesign etoolbox csquotes ly1 hyphenat
```

## Mount some network drives

```
apt-get install cifs-utils
```

add to `/etc/fstab`:

```
//192.168.167.200/Rasmus /mnt/cissi/Rasmus cifs user,uid=rasmus,rw,suid,credentials=/etc/cifspwd 0 0
//192.168.167.200/Public /mnt/cissi/Public cifs user,uid=rasmus,rw,suid,credentials=/etc/cifspwd 0 0
```

add to `/etc/cifspwd`:

```
username=Rasmus
password=...
```

## Dependencies for compiling matplotlib

```
apt-get install pkg-config libpng12-dev libfreetype6-dev
```


## PDF tools

```
apt-get install pdfmod pdftk
```


## R

```
sudo apt-get install r-base-core
```

And to get Jupyter/R going (http://irkernel.github.io/installation/):

```
pip install ipython[notebook]
sudo apt-get install libzmq3-dev
```

and in R something like

```
install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
                 repos = c('http://irkernel.github.io/', getOption('repos')),
                 type = 'source')
IRkernel::installspec()
```

