import flet as f
from flet import page


def main(page: page):
    page.title = "Login to PMS"
    page.padding = 50
    page.theme_mode = f.ThemeMode.LIGHT
    page.window_max_width = 500
    page.window_max_height = 400
    # page.theme = f.Theme(use_material3=True, color_scheme_seed=f.colors.AMBER)
    # page.bgcolor = f.colors.WHITE70
    page.color = f.colors.BLACK

    def LoginBtnCicked(e):
        pass

    Email = f.TextField(width=300, hint_text="Email",
                        color=f.colors.BLACK,
                        hint_style=f.TextStyle(color=f.colors.BLACK), label="Email")

    Password = f.TextField(width=300, hint_text="Password", password=True,
                           color=f.colors.BLACK,
                           hint_style=f.TextStyle(color=f.colors.BLACK), label="Password",)
    LoginBTn = f.ElevatedButton(
        text="Login", icon=f.icons.LOGIN_ROUNDED, on_click=LoginBtnCicked)

    img = f.Image(visible=True,
                  src=f"/img/pic.png",
                  width=400,
                  height=400,
                  fit=f.ImageFit.FILL,
                  )

    page.add(f.Column(
        [
            f.Row([
                f.IconButton(
                    f.icons.ADD_CARD,
                    icon_color=f.colors.BLUE,
                ),
                f.Text("Login To PMS",
                       bgcolor=None,
                       color=f.colors.BLUE,
                       weight=f.FontWeight.BOLD,
                       size=35),
                f.Icon(f.icons.LOGIN,
                       color=f.colors.RED,
                       ),
            ],
                alignment=f.MainAxisAlignment.SPACE_BETWEEN),
            f.Row([
                f.Column([
                    Email, Password, LoginBTn
                ],
                    height=400, width=300, alignment=f.MainAxisAlignment.CENTER,
                ),
                f.Column([
                    img,
                ],),
            ]),
        ]
    ))
    page.update()


app = f.app(target=main, assets_dir="assets", view="flet_app")
