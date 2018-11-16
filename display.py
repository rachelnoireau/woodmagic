from tkinter import *
import sys
import os

import time
from agent import Action
from wood import Wood


class Display:

    def __init__(self, agent, wood):
        self.agent = agent
        self.wood = wood

        self.agent_pos = self.agent.get_pos()

        self.cv = 0
        self.grid = 0

        self.CELL_SIZE = 650/(self.agent.level + 3)

        self.window = Tk()
        self.window.title("Magic Wood")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        #self.cristal_photo = PhotoImage(file=self.resource_path("img/cristal.png"))
        self.hero_photo = PhotoImage(file=self.resource_path("img/hero.png"))
        self.hole_photo = PhotoImage(file=self.resource_path("img/hole.png"))
        self.monster_photo = PhotoImage(file=self.resource_path("img/monster.png"))
        self.pooh_photo = PhotoImage(file=self.resource_path("img/pooh.png"))
        self.portal_photo = PhotoImage(file=self.resource_path("img/portal.png"))
        self.wind_photo = PhotoImage(file=self.resource_path("img/wind.png"))

        self.cv = Canvas(self.window, width=650, height=650, bd=0)
        self.add_grid(self.wood.get_grid())
        self.create_button()

        self.start_loop()

    def add_grid(self, grid):
        self.window.grid_size()
        self.grid = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.draw_area(grid[j][i])

        self.draw_agent()

    def draw_area(self, area):
        self.cv.create_rectangle(area.posX * self.CELL_SIZE,
                            area.posY * self.CELL_SIZE,
                            (area.posX + 1) * self.CELL_SIZE,
                            (area.posY + 1) * self.CELL_SIZE,
                            fill='white')

        if area.is_next_to_monster:
            self.cv.create_image(area.posX * self.CELL_SIZE + 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.pooh_photo)

        if area.is_monster:
            self.cv.create_image(area.posX * self.CELL_SIZE + 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.monster_photo)

        if area.is_next_to_hole:
            self.cv.create_image(area.posX * self.CELL_SIZE + self.CELL_SIZE / 2 - 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.wind_photo)

        if area.is_hole:
            self.cv.create_image(area.posX * self.CELL_SIZE + self.CELL_SIZE / 2 - 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.hole_photo)

        if area.is_portal:
            self.cv.create_image(area.posX * self.CELL_SIZE + self.CELL_SIZE / 2 - 1,
                            area.posY * self.CELL_SIZE + 1,
                            anchor=NW, image=self.portal_photo)

        self.cv.grid(row=area.posX, column=area.posY)

    def will_die(self):
        if self.grid[self.agent.get_pos()[1]][self.agent.get_pos()[0]].get_monster():
            return True
        if self.grid[self.agent.get_pos()[1]][self.agent.get_pos()[0]].get_hole():
            return True
        return False

    def call_act(self):
        self.agent.plan_next_action()
        action_performed = self.agent.execute_action()
        print(action_performed)

        print(actionPerformed)

        if not(self.agent_pos == self.agent.get_pos()):
            self.agent_pos = self.agent.get_pos()

        self.update_window()
        self.window.update()

        if self.will_die():
            self.agent.is_dead()
            self.agent.set_pos(0, 0)
            self.agent_pos = self.agent.get_pos()

            time.sleep(2)
            self.update_window()

        if self.agent.next_area_to_visit.get_is_next_to_monster() and action_performed == Action.USE_CRISTAL:
            pos_direction_cristal = (self.agent.next_area_to_visit.posX, self.agent.next_area_to_visit.posY)
            self.grid[ pos_direction_cristal[1]][ pos_direction_cristal[0]].kill_monster()

            time.sleep(2)
            self.update_window()

        if self.agent.current_area.get_portal() and action_performed == Action.TAKE_PORTAL:
            self.agent.next_level()
            self.agent.set_pos(0, 0)
            self.wood = Wood(self.agent.level + 3)
            self.agent.current_area = self.wood.get_area_at_position(0, 0)
            self.agent_pos = (self.agent.current_area.posX, self.agent.current_area.posY)
            self.grid = self.wood.get_grid()
            self.CELL_SIZE = 650 / (self.agent.level + 3)

            time.sleep(2)
            self.update_window()

    def update_window(self):
            self.cv.delete("all")
            self.add_grid(self.wood.get_grid())
            self.grid = self.wood.get_grid()

    def create_button(self):
        Button(text="next action", command=self.call_act).grid(sticky=S)

    def draw_agent(self):
        x_agent = int(1 + self.CELL_SIZE * self.agent.get_pos()[0])
        y_agent = int(1 + self.CELL_SIZE * self.agent.get_pos()[1])
        # resize the image
        hero_photo = self.hero_photo
        scale_w = (self.hero_photo.width() / self.CELL_SIZE)*2
        scale_h = (self.hero_photo.height() / self.CELL_SIZE)*2
        hero_photo = hero_photo.zoom(1).subsample(int(scale_w)+1, int(scale_h)+1)
        self.agent_image = self.cv.create_image(x_agent, y_agent, anchor=NW, image=self.hero_photo)
        self.cv.grid(row=1, column=x_agent - 1)

    def on_closing(self):
        self.window.destroy()

    def start_loop(self):
        self.window.mainloop()

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)