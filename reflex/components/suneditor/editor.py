from reflex.components.component import NoSSRComponent, Component
from reflex.vars import Var
from reflex.utils.imports import ImportDict, ImportVar
from reflex.utils.format import to_camel_case
from reflex.base import Base
from typing import Any

class EditorOptions(Base):
    button_list: list[list[str] | str] | None = None
    default_tag: str | None = None
    mode: str | None = None
    rtl: bool | None = None

class SimpleEditor(NoSSRComponent):

    library = "suneditor-react@3.6.1"
    tag = "SunEditor"
    is_default = True
    lib_dependencies = ["suneditor"]

    set_contents: Var[str]
    placeholder: Var[str]
    height: Var[str]

    def add_imports(self) -> ImportDict:
        return {
            "": ImportVar(tag="suneditor/dist/css/suneditor.min.css", install=False)
        }

    @classmethod
    def create(cls, set_options: EditorOptions | None = None, **props: Any) -> Component:
        if set_options is not None:
            if isinstance(set_options, Var):
                raise ValueError("EditorOptions cannot be a state Var")
            props["set_options"] = {
                to_camel_case(k): v
                for k, v in set_options.dict().items()
                if v is not None
            }
        return super().create(*[], **props)
