from kivy.app import App
from kivy.uix.widget import Widget


class LabWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LabApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def main() -> int:
    try:

        lab_app: LabApp = LabApp()
        lab_widget: LabWidget = LabWidget()

        lab_app.run()

    except Exception as e:
        print(f"Exception Thrown: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
