# ./point_manager.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-08-23 15:00:52.826247 by PyXB version 1.2.4 using Python 3.5.2.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ad6a9f28-6974-11e6-8a50-000c29ae0b70')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 4, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Sensor uses Python identifier Sensor
    __Sensor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Sensor'), 'Sensor', '__AbsentNamespace0_CTD_ANON_Sensor', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 6, 16), )

    
    Sensor = property(__Sensor.value, __Sensor.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 33, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 33, 12)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute ts uses Python identifier ts
    __ts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ts'), 'ts', '__AbsentNamespace0_CTD_ANON_ts', pyxb.binding.datatypes.string, required=True)
    __ts._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 34, 12)
    __ts._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 34, 12)
    
    ts = property(__ts.value, __ts.set, None, None)

    
    # Attribute NoSensors uses Python identifier NoSensors
    __NoSensors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NoSensors'), 'NoSensors', '__AbsentNamespace0_CTD_ANON_NoSensors', pyxb.binding.datatypes.integer, required=True)
    __NoSensors._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 35, 12)
    __NoSensors._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 35, 12)
    
    NoSensors = property(__NoSensors.value, __NoSensors.set, None, None)

    _ElementMap.update({
        __Sensor.name() : __Sensor
    })
    _AttributeMap.update({
        __id.name() : __id,
        __ts.name() : __ts,
        __NoSensors.name() : __NoSensors
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 7, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Age uses Python identifier Age
    __Age = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Age'), 'Age', '__AbsentNamespace0_CTD_ANON__Age', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 9, 28), )

    
    Age = property(__Age.value, __Age.set, None, None)

    
    # Element Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Status'), 'Status', '__AbsentNamespace0_CTD_ANON__Status', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 10, 28), )

    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Element Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Service'), 'Service', '__AbsentNamespace0_CTD_ANON__Service', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 11, 28), )

    
    Service = property(__Service.value, __Service.set, None, None)

    
    # Element Point uses Python identifier Point
    __Point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Point'), 'Point', '__AbsentNamespace0_CTD_ANON__Point', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 12, 28), )

    
    Point = property(__Point.value, __Point.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON__id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 25, 24)
    __id._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 25, 24)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON__type', pyxb.binding.datatypes.integer, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 26, 24)
    __type._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 26, 24)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute snid uses Python identifier snid
    __snid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'snid'), 'snid', '__AbsentNamespace0_CTD_ANON__snid', pyxb.binding.datatypes.string, required=True)
    __snid._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 27, 24)
    __snid._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 27, 24)
    
    snid = property(__snid.value, __snid.set, None, None)

    
    # Attribute batt uses Python identifier batt
    __batt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'batt'), 'batt', '__AbsentNamespace0_CTD_ANON__batt', pyxb.binding.datatypes.integer, required=True)
    __batt._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 28, 24)
    __batt._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 28, 24)
    
    batt = property(__batt.value, __batt.set, None, None)

    
    # Attribute battlife uses Python identifier battlife
    __battlife = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'battlife'), 'battlife', '__AbsentNamespace0_CTD_ANON__battlife', pyxb.binding.datatypes.string, required=True)
    __battlife._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 29, 24)
    __battlife._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 29, 24)
    
    battlife = property(__battlife.value, __battlife.set, None, None)

    _ElementMap.update({
        __Age.name() : __Age,
        __Status.name() : __Status,
        __Service.name() : __Service,
        __Point.name() : __Point
    })
    _AttributeMap.update({
        __id.name() : __id,
        __type.name() : __type,
        __snid.name() : __snid,
        __batt.name() : __batt,
        __battlife.name() : __battlife
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 13, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__AbsentNamespace0_CTD_ANON_2_Value', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 15, 40), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_2_id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 17, 36)
    __id._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 17, 36)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_2_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 18, 36)
    __type._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 18, 36)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute dtype uses Python identifier dtype
    __dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dtype'), 'dtype', '__AbsentNamespace0_CTD_ANON_2_dtype', pyxb.binding.datatypes.integer, required=True)
    __dtype._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 19, 36)
    __dtype._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 19, 36)
    
    dtype = property(__dtype.value, __dtype.set, None, None)

    
    # Attribute ptid uses Python identifier ptid
    __ptid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptid'), 'ptid', '__AbsentNamespace0_CTD_ANON_2_ptid', pyxb.binding.datatypes.string, required=True)
    __ptid._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 20, 36)
    __ptid._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 20, 36)
    
    ptid = property(__ptid.value, __ptid.set, None, None)

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__AbsentNamespace0_CTD_ANON_2_index', pyxb.binding.datatypes.integer, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 21, 36)
    __index._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 21, 36)
    
    index = property(__index.value, __index.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        __id.name() : __id,
        __type.name() : __type,
        __dtype.name() : __dtype,
        __ptid.name() : __ptid,
        __index.name() : __index
    })



Point_Manager = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Point_Manager'), CTD_ANON, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 3, 4))
Namespace.addCategoryObject('elementBinding', Point_Manager.name().localName(), Point_Manager)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Sensor'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 6, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Sensor')), pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 6, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Age'), pyxb.binding.datatypes.integer, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 9, 28)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Status'), pyxb.binding.datatypes.integer, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 10, 28)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Service'), pyxb.binding.datatypes.integer, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 11, 28)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Point'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 12, 28)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Age')), pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 9, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Status')), pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 10, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Service')), pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 11, 28))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'Point')), pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 12, 28))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Value'), pyxb.binding.datatypes.float, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 15, 40)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'Value')), pyxb.utils.utility.Location('/home/servilla/python/3.5/pyxb_test/Point_Manager.xsd', 15, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

