# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2012 - 2013 Therp BV (<http://therp.nl>).
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Apply a tax on bank statement lines',
    'version': '0.1',
    'license': 'AGPL-3',
    'author': 'Therp BV',
    'website': 'https://launchpad.net/banking-addons',
    'category': 'Banking addons',
    'depends': [
        'account',
        ],
    'data': [
        'view/account_bank_statement.xml',
    ],
    'description': '''
Allow an (inclusive) tax to be set on a bank statement line. When the
statement is configured, the tax will be processed like on a move line.
    ''',
    'installable': True,
}
