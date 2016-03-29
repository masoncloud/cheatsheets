# Vim

### View data as hexdump -C

    :% ! xxd

### Disable hex view

    :% ! xxd -r

### Split window with new file open

    :split <filename><CR>
    # Switch via ^Ww

### Auto complete menu on seen text

    ctrl-p

### Display line numbers

    # While running VIM
    :set number
    :set nu

    # To disable
    :set nonumber
    :set nonu

    # Toggle display
    :set nu!

In vimrc

    set number

Stylizing
    
    # gutter width
    :set numberwidth=3

    # Color
    :highlight LineNr term=bold cterm=NONE ctermfg=DarkGrey ctermbg=LightBlue gui=NONE guifg=DarkGrey guibg=LightGrey

### Pathogen/dotfiles setup

    mv ~/.vimrc ~/.vim/vimrc
    ln -s ~/.vim/vimrc ~/.vimrc
    cd ~/.vim
    git init
    # Create readme.md, see example: https://raw.githubusercontent.com/nelstrom/dotvim/master/README
    
    # Setup pathogen
    mkdir ~/.vim/autoload
    curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
    # Add the following to vimrc
    call pathogen#infect()
    call pathogen#helptags()

### Install dracula theme with git submodules and pathogen

    cd ~/.vim
    git submodule add https://github.com/zenorocha/dracula-theme.git bundle/dracula-theme

### Airline

    git clone https://github.com/vim-airline/vim-airline ~/.vim/bundle/vim-airline
    # in vimrc
    set laststatus=2

### Fugitive (git integration)

    git clone https://github.com/tpope/vim-fugitive.git ~/.vim/bundle/vim-fugitive
    cd ~/.vim/bundle
    vim -u NONE -c "helptags vim-fugitive/doc" -c q

### VirtualEnv

    git clone https://github.com/jmcantrell/vim-virtualenv.git ~/.vim/bundle/vim-virtualenv

