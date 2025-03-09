import math

from z1.plugins.plugin import Plugin
from z1.params.ligationType import LigationType
from z1.helpers.svg import Svg

class OrganicPlugin(Plugin):
	def __init__(self, code:str):
		super(OrganicPlugin, self).__init__(code)

	def write_atoms(self, svg:Svg) -> Svg:
		for atom in self.atoms:
			[symbol, x, y, index] = atom

			if symbol == 'C':
				continue

			if symbol == 'H':
				my_ligations = list(filter(lambda ligation: ligation[3][1] == index, self.ligations))
				group = my_ligations[0][3]
				another_atom = self.atoms[ group[0] ]
				if another_atom[0] == 'C':
					continue

			svg.text(symbol, x + self.center_x, y + self.center_y)

		return svg

	def calculate_lines(self, a:int, b:int, angle:float, wave = [(0,0,0,0)]):
		ax = self.atoms[a][1] + self.center_x
		ay = self.atoms[a][2] + self.center_y
		bx = self.atoms[b][1] + self.center_x
		by = self.atoms[b][2] + self.center_y

		for (f, t, df, dt) in wave:
			x1 = ax + math.cos( math.pi * (angle+f) / 180.0 ) * df
			y1 = ay + math.sin( math.pi * (angle+f) / 180.0 ) * df
			x2 = bx + math.cos( math.pi * (angle+180+t) / 180.0 ) * dt
			y2 = by + math.sin( math.pi * (angle+180+t) / 180.0 ) * dt
			yield x1, y1, x2, y2

	def write_ligations(self, svg):
		for ligation in self.ligations: 
			angle, eletrons, type, group = ligation

			if type == LigationType.IONICA:
				continue

			#! for some reason *_ solves the bug '-'
			a, b, *_ = group
			atom_from = self.atoms[a]
			atom_to = self.atoms[b]

			if atom_from[0] == 'C' and atom_to[0] == 'H':
				continue

			ligation_distance_from = self.ligation_distance_from_atom
			ligation_distance_to = self.ligation_distance_from_atom

			if atom_from[0] == 'C':
				ligation_distance_from = 0

			if atom_to[0] == 'C':
				ligation_distance_to = 0

			wave = [(0, 0, ligation_distance_from, ligation_distance_to)]

			match eletrons:
				case 2:
					sum_from = self.ligation_distance_from_ligation
					sum_to = self.ligation_distance_from_ligation

					if ligation_distance_from == 0:
						ligation_distance_from = 1
						sum_from = 90
					
					if ligation_distance_to == 0:
						ligation_distance_to = 1
						sum_to = 90

					wave = [ (sum_from, -sum_to, ligation_distance_from, ligation_distance_to), (-sum_from, sum_to, ligation_distance_from, ligation_distance_to) ]

				case 3:
					sum_from = self.ligation_distance_from_ligation
					sum_to = self.ligation_distance_from_ligation

					if ligation_distance_from == 0:
						ligation_distance_from = 1
						sum_from = 90
					
					if ligation_distance_to == 0:
						ligation_distance_to = 1
						sum_to = 90

					wave = [ (sum_from, -sum_to, ligation_distance_from, ligation_distance_to), (0, 0, ligation_distance_from, ligation_distance_to) ,(-sum_from, sum_to, ligation_distance_from, ligation_distance_to) ]

			for ax, ay, bx, by in self.calculate_lines(a, b, angle, wave):
				svg.line(ax, ay, bx, by)

		return svg
	
	def get_bounds(self):
		small_x = 0
		small_y = 0
		big_x = 0
		big_y = 0

		for [symbol, x, y, index] in self.atoms:
			if symbol == 'H':
				my_ligations = list(filter(lambda ligation: ligation[3][1] == index, self.ligations))
				group = my_ligations[0][3]
				another_atom = self.atoms[ group[0] ]
				if another_atom[0] == 'C':
					continue

			if small_x > x:
				small_x = x

			if small_y > y:
				small_y = y

			if big_x < x:
				big_x = x
				
			if big_y < y:
				big_y = y

		cwidth = big_x + -small_x
		cheight = big_y + -small_y

		center_x = -small_x + self.border
		center_y = -small_y + self.border
		center = (center_x, center_y)

		width = cwidth + self.border * 2
		height = cheight + self.border * 2
		size = (width, height)

		return size, center
