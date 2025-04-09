from esphome.components import select
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_OPTIONS
from . import INTELLIFLO_CHILD_SCHEMA, CONF_INTELLIFLO_ID

DEPENDENCIES = ["pentair_intelliflo"]

CONF_PUMPMODE = "pump_mode"
CONF_SELECTS = [
    "Local",
    "Regulated RPM",
    "Regulated Flow",
]

intelliflo_ns = cg.esphome_ns.namespace("intelliflo")

IntellifloComponent = intelliflo_ns.class_("Intelliflo", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_PUMPMODE): select.select_schema(
          IntellifloComponent
        ),
    }
).extend(INTELLIFLO_CHILD_SCHEMA)


async def to_code(config):
    var = await cg.get_variable(config[CONF_INTELLIFLO_ID])
    if pumpmode_config := config.get(CONF_PUMPMODE):
        sel = await select.new_select(
            pumpmode_config,
            options=[CONF_SELECTS],
        )
        cg.add(var.set_operating_mode_select(sel))
