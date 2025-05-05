from kivy.app import App


class LabApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def main() -> int:
    lab_app: LabApp = LabApp()
    lab_app.get_running_app()

    return 0


if __name__ == "__main__":
    main()
