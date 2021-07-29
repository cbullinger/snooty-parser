import docutils.nodes
import docutils.utils
from typing import Any, Optional, List, Iterable, Union
from typing_extensions import Protocol


def unescape(text: str) -> str: ...


def make_id(input_value: str) -> str: ...


def fully_normalize_name(name: str) -> str: ...


def whitespace_normalize_name(name: str) -> str: ...


class NodeVisitor(Protocol):
    def dispatch_visit(self, node: docutils.nodes.Node) -> None: ...
    def dispatch_departure(self, node: docutils.nodes.Node) -> None: ...


class Node:
    source: Optional[str]
    line: Optional[int]
    parent: Optional[Node]
    document: Optional[Node]
    children: List[Node]

    def walkabout(self, visitor: NodeVisitor) -> None: ...
    def astext(self) -> str: ...

    def __getitem__(self, key: Union[int, str]) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __contains__(self, key: str) -> bool: ...


def dupname(node: Node, name: str) -> None: ...


class Root: ...


class Body: ...


class Inline: ...


class Labeled: ...


class PreBibliographic: ...


class Titular: ...


class General(Body): ...


class Special(Body): ...


class BackLinkable:
    def add_backref(self, refid: str) -> None: ...


class Invisible(PreBibliographic): ...


class Targetable(Resolvable): ...


class Element(Node):
    def __init__(self, rawsource: str='', *children: Node, **attribute: object) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def append(self, node: Node) -> None: ...
    def extend(self, nodes: Iterable[Node]) -> None: ...


class TextElement(Element):
    def __init__(self, rawsource: str='', text: str='', *children: Node, **attribute: object) -> None: ...


class FixedTextElement(TextElement): ...


class Structural: ...


class document(Root, Structural, Element):
    reporter: docutils.utils.Reporter


class TreePruningException(Exception): ...


class SkipNode(TreePruningException): ...


class SkipDeparture(TreePruningException): ...


class SkipChildren(TreePruningException): ...


class system_message(Element): ...


class Text(Node):
    def __init__(self, data: object, rawsource: str=''): ...


class Resolvable:
    resolved: int


class Referential(Resolvable): ...


class reference(General, Inline, Referential, TextElement): ...


class Part: ...


class Sequential(Body): ...


class bullet_list(Sequential, Element): ...


class enumerated_list(Sequential, Element): ...


class list_item(Part, Element): ...


class strong(Inline, TextElement): ...


class emphasis(Inline, TextElement): ...


class literal(Inline, TextElement): ...


class field(Part, Element): ...


class definition(Part, Element): ...


class field_list(Sequential, Element): ...


class block_quote(General, Element): ...


class target(Special, Invisible, Inline, TextElement, Targetable): ...


class definition_list(Sequential, Element): ...


class definition_list_item(Part, Element): ...


class title(Titular, PreBibliographic, TextElement): ...


class substitution_definition(Special, Invisible, TextElement): ...


class substitution_reference(Inline, TextElement): ...


class footnote(General, BackLinkable, Element, Labeled, Targetable): ...


class footnote_reference(Inline, Referential, TextElement): ...


class section(Structural, Element): ...


class paragraph(General, TextElement): ...


class comment(Special, Invisible, FixedTextElement): ...


class literal_block(General, FixedTextElement): ...


class term(Part, TextElement): ...


class classifier(Part, TextElement): ...


class line_block(General, Element): ...


class line(Part, TextElement): ...


class transition(Structural, Element): ...


class table(General, Element): ...


class problematic(Inline, TextElement): ...


class label(Part, TextElement): ...

class field_name(Part, TextElement): ...

class field_body(Part, Element): ...
