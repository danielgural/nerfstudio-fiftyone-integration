import fiftyone as fo
import fiftyone.operators as foo
import fiftyone.operators.types as types

NERFSTUDIO_URL = "http://0.0.0.0:7007 "


class NerfStudio_Panel(foo.Panel):
    @property
    def config(self):
        return foo.PanelConfig(
            name="NerfStudio_Panel",
            label="View Your Assets in NerfStudio",
            icon="/assets/atom.svg",
            surfaces="modal"
        )

    def on_load(self, ctx):
        pass

    def render(self, ctx):
        panel = types.Object()

        panel.define_property(
            "frame",
            types.String(),
            view=types.HeaderView(
                label="x",
                align_x="center",
                align_y="center",
                componentsProps={
                    "headingsContainer": {"overflow": "hidden"},
                    "label": {
                        "component": "iframe",
                        "src": NERFSTUDIO_URL,
                        "width": "800px",
                        "height": "500px",
                        "border": "none",
                    },
                },
            ),
        )
            
        return types.Property(panel, view=types.GridView())
    
    def on_change_config(self, ctx):
        pass
    
def register(p):
    p.register(NerfStudio_Panel)