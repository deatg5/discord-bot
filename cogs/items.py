import discord
import random
from random import randint
from discord.ext import commands

class Items(commands.Cog):

    def __init__(self, client):
        self.client = client

    item_list = [
        {
        	'id': 1,
            'name': 'egg',
        	'friendly_name': 'Egg',
            'description': 'Can I offer you a nice egg in this trying time?',
        	'use_messages': ['Here are your eggs, sir!'],
        	'consume_chance': 1.0,
        	'cost': 10,
        	'sell_price': 1,
        	'rarity': 'Common',
            'battle_use_messages': [],
            'damage': 0,
            'heal_amount': 100,
            'emoji': '<:egg:932701745287688262>'
        },
        {
        	'id': 2,
            'name': 'terrydrawing',
        	'friendly_name': 'Drawing of Terry Crews',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 0.2,
        	'cost': 1000,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 120,
            'heal_amount': 0,
            'emoji': '<:drawingofterrycrews:932701768977113208>'
        },
        {
        	'id': 3,
            'name': 'soup',
        	'friendly_name': 'Soup',
            'description': 'Yummy soup',
        	'use_messages': ['Soup time!', 'soup time'],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [],
            'damage': 0,
            'heal_amount': 0,
            'emoji': '<:soup:932701769161641994>'
        },
        {
        	'id': 4,
            'name': 'the',
        	'friendly_name': '**The**',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 0.0,
        	'cost': 0,
        	'sell_price': 250000,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': '<:the:932701899965206588>'
        },
        {
        	'id': 5,
            'name': 'lasaga',
        	'friendly_name': 'Lasaga',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 100,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 6,
            'name': 'laptop',
        	'friendly_name': '$15 Laptop from Wish.com',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 0.02,
        	'cost': 15000,
        	'sell_price': 300,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 7,
            'name': 'brazil',
        	'friendly_name': 'Brazil',
            'description': 'Come to Brazil!',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 8,
            'name': 'keyboardcontroller',
        	'friendly_name': 'GameCube Keyboard Controller',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 9,
            'name': 'godstatue',
        	'friendly_name': 'God Statue',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 10,
            'name': 'demfextablet',
        	'friendly_name': 'Demfex Tablet',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 11,
            'name': 'dinnerblaster',
        	'friendly_name': 'Dinner Blaster',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 12,
            'name': 'salad',
        	'friendly_name': 'Pizza Pasta Salad With Chicken Breast Halves',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 13,
            'name': 'tree',
        	'friendly_name': 'Tree',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 14,
            'name': 'sledgehammer',
        	'friendly_name': 'Sledgehammer',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 15,
            'name': 'cableandrouter',
        	'friendly_name': 'Network Cable and Router',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 16,
            'name': 'sqlsoup',
        	'friendly_name': 'Derek\'s SQL Soup',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 17,
            'name': 'bup',
        	'friendly_name': 'BUP',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 18,
            'name': 'hemoglobin',
        	'friendly_name': 'Hemoglobin',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 19,
            'name': 'compressedair',
        	'friendly_name': 'Compressed Air',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 20,
            'name': 'harpoon',
        	'friendly_name': 'Harpoon',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 21,
            'name': 'manymanymeats',
        	'friendly_name': 'Many Many Meats',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 22,
            'name': 'manymanymeatsflavourful',
        	'friendly_name': 'Many Many Meats (Flavourful)',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 23,
            'name': 'buttor',
        	'friendly_name': 'Buttor',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 24,
            'name': 'ape',
        	'friendly_name': 'Ape',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 25,
            'name': 'recyclebin',
        	'friendly_name': 'Recycle Bin',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 26,
            'name': 'stopsign',
        	'friendly_name': 'Stop Sign',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 27,
            'name': 'spongebob',
        	'friendly_name': 'SpongeBob SquarePants',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 28,
            'name': 'sign',
        	'friendly_name': 'Sign',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 29,
            'name': 'donkeykongbarrelblast',
        	'friendly_name': 'Donkey Kong Barrel Blast',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 30,
            'name': 'femboy',
        	'friendly_name': 'Femboy',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 31,
            'name': 'spritecranberry',
        	'friendly_name': 'Sprite® Cranberry',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 32,
            'name': 'fidgetspinner',
        	'friendly_name': 'Fidget Spinner',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 33,
            'name': 'glassofwater',
        	'friendly_name': 'Glass of Water',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 34,
            'name': 'brainage',
        	'friendly_name': 'Brain Age',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 35,
            'name': 'tire',
        	'friendly_name': 'Tire',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 36,
            'name': 'glassofmilk',
        	'friendly_name': 'Glass of Milk',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': ['Empowered by the Baltic God of Milk, you feel the shredded cheese course through your veins. You grow stronger.'],
            'damage': 0,
            'heal_amount': 150,
            'emoji': ''
        },
        {
        	'id': 37,
            'name': 'jollizoom',
        	'friendly_name': 'Jollizoom',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 38,
            'name': 'bingus',
        	'friendly_name': 'Bingus',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 39,
            'name': 'totemofundying',
        	'friendly_name': 'Totem of Undying',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 40,
            'name': 'nautilusshell',
        	'friendly_name': 'Nautilus Shell',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 41,
            'name': 'warioshamburger',
        	'friendly_name': 'Wario\'s Hamburger',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
        	'id': 42,
            'name': 'headphones',
        	'friendly_name': 'Headphones',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0,
            'emoji': ''
        },
        {
            'id': 43,
            'name': 'cyanpurpleobject',
            'friendly_name': 'Cyan and Purple Object',
            'description': 'A unknown cyan and purple Object',
            'use_messages': ['idk'],
            'consume_chance': 1.0,
            'cost': 1000,
            'sell_price': 950,
            'rarity': 'Rare',
            'battle_use_messages': [''],
            'damage': 50,
            'heal_amount': 25,
            'emoji': ''
        },
        {
            'id': 44,
            'name': 'coil',
            'friendly_name': 'Roll of Air Conditioning Pair Coil 1/4\' x 3/8\' 410A 20m Polyethylene UV protected Insulated Copper heat resistant to 120°c',
            'description': '',
            'use_messages': [''],
            'consume_chance': 1.0,
            'cost': 1000,
            'sell_price': 950,
            'rarity': 'Rare',
            'battle_use_messages': [''],
            'damage': 50,
            'heal_amount': 25,
            'emoji': ''
        }
    ]

def setup(client):
    client.add_cog(Items(client))


