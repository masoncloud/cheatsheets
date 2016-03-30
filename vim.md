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

## Navigating

### Movements

Mnemonics:

* Up
* Down
* Forward
* Back
* Home
* Middle
* Last

    ctrl+u: half-page up
    ctrl+d: half-page down
    ctrl+b: page up
    ctrl+f: page down

    z return: current line to top of screen
    NNz return: move line number (NN) to top of screen
    z.: current line to middle of screen
    z-: current line to bottom of screen

    H: moves cursor to top of screen
    M: moves cursor to middle of screen
    L: moves cursor to bottom of screen
    
    e: move to end of word
    b: move back a word
    w: moves forward to start of next word

    E: move to end of word, ignoring symbols
    B: move back a word, ignoring symbols
    W: moves forward to start of next word, ignoring symbols
    
## File operations

### Save currently open file with different name

    :saveas

### Launch file explorer

    :Explore
    :e.

    # In split mode (short for split explore)
    :Sex

    # In vertical split mode
    :Vex

## Window operations

### Split pane movements
    
    :split <filename> ::split window and open other file in it
    :vsplit <filename> ::vertically split window and open other file in it

    ctrl+w <direction>: Move focus to pane in arrow direction
    ctrl+w q: Close a window
    ctrl+w o: Close all windows except current
    :on same as above

## Text manipulations

### Copy & pasting

    y$: Copy text to from cursor position to end of current line (yank)
    p: Paste text in copy buffer
