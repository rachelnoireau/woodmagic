from tkinter import *
import sys
import os


class Display:

    CELL_SIZE = 50

    def __init__(self , size):
        self.agent_pos = (0,0)

        self.CELL_SIZE = 600/size

        #self.room_changes_q = room_changes_q
        #self.agent_move_q = agent_move_q
        #self.disp_to_agent_q = disp_to_agent_q

        self.window = Tk()
        self.window.title("Magic Wood")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.canvas_list = []
        self.arrow_list = []

        self.cristal_photo = PhotoImage(file=self.resource_path("img/cristal.png"))
        self.hero_photo = PhotoImage(file=self.resource_path("img/hero.png"))
        self.hole_photo = PhotoImage(file=self.resource_path("img/hole.png"))
        self.monster_photo = PhotoImage(file=self.resource_path("img/monster.png"))
        self.pooh_photo = PhotoImage(file=self.resource_path("img/pooh.png"))
        self.portal_photo = PhotoImage(file=self.resource_path("img/portal.png"))
        self.wind_photo = PhotoImage(file=self.resource_path("img/wind.png"))


		
    def add_grid(self, grid):
        self.window.grid_size()
        new_canvas = Canvas(self.window, width=600, height=600, bd=0)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.draw_area(new_canvas, grid[j][i])

        self.draw_agent(new_canvas)
        self.canvas_list.append(new_canvas)



    def draw_area(self, cv, area):
        cv.create_rectangle(area.posX * self.CELL_SIZE,
                            area.posY * self.CELL_SIZE,
                            (area.posX + 1) * self.CELL_SIZE,
                            (area.posY + 1) * self.CELL_SIZE,
                            fill='white')
        if area.is_monster:
            cv.create_image(area.posX * self.CELL_SIZE + 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.monster_photo)
        if area.is_next_to_monster:
            cv.create_image(area.posX * self.CELL_SIZE + 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.pooh_photo)


        if area.is_hole:
            cv.create_image(area.posX * self.CELL_SIZE + self.CELL_SIZE / 2 - 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.hole_photo)
        if area.is_next_to_hole:
            cv.create_image(area.posX * self.CELL_SIZE + self.CELL_SIZE / 2 - 1,
                            area.posY * self.CELL_SIZE + self.CELL_SIZE / 2,
                            anchor=NW, image=self.wind_photo)

        cv.grid(row=area.posX, column=area.posY)#, padx=self.CELL_SIZE/2, pady=self.CELL_SIZE/2
	
    def callAct(self):
        print("prochaine action")
	
    def create_button(self):
        Button(text ="next action", command = self.callAct).grid(sticky=S)

    def draw_agent(self, cv):
        x_agent = int(1 + self.CELL_SIZE * self.agent_pos[0])
        y_agent = int(1 + self.CELL_SIZE * self.agent_pos[1])
        #resize the image
        hero_photo = self.hero_photo
        scale_w = (self.hero_photo.width() / self.CELL_SIZE)*2
        scale_h = (self.hero_photo.height() / self.CELL_SIZE)*2
        hero_photo = hero_photo.zoom(1).subsample(int(scale_w)+1, int(scale_h)+1)
        self.agent_image = cv.create_image(x_agent, y_agent, anchor=NW, image=self.hero_photo)
        cv.grid(row=1, column=x_agent -1)



    def on_closing(self):
        self.window.destroy()

    def start_loop(self):
        #self.window.after(1, self.check_for_changes)
        self.window.mainloop()

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)