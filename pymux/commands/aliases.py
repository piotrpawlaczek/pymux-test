"""
Aliases for all commands.
(On purpose kept compatible with tmux.)
"""
from __future__ import unicode_literals

__all__ = (
    'ALIASES',
)


ALIASES = {
    'bind': 'bind-key',
    'breakp': 'break-pane',
    'clearhist': 'clear-history',
    'confirm': 'confirm-before',
    'detach': 'detach-client',
    'display': 'display-message',
    'displayp': 'display-panes',
    'killp': 'kill-pane',
    'killw': 'kill-window',
    'lastp': 'last-pane',
    'last': 'last-window',
    'lsk': 'list-keys',
    'lsp': 'list-panes',
    'movew': 'move-window',
    'neww': 'new-window',
    'lextl': 'next-layout',
    'next': 'next-window',
    'pasteb': 'paste-buffer',
    'prevl': 'previous-layout',
    'prev': 'previous-window',
    'rename': 'rename-session',
    'renamew': 'rename-window',
    'resizep': 'resize-pane',
    'rotatew': 'rotate-window',
    'selectl': 'select-layout',
    'selectp': 'select-pane',
    'selectw': 'select-window',
    'send': 'send-keys',
    'set': 'set-option',
    'source': 'source-file',
    'splitw': 'split-window',
    'suspendc': 'suspend-client',
    'swapp': 'swap-pane',
    'unbind': 'unbind-key',
}
