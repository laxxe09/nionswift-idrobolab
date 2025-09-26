from .BasicImageProcessingPanel import BasicImageProcessingPanel

def run(api_broker) -> None:
    """Called when the plug-in is loaded by Nion Swift."""
    api_broker.panel_type_registry.register_panel(
        "basic_image_processing_panel",   
        "Basic Image Processing",         
        BasicImageProcessingPanel        
    )

def stop(api_broker) -> None:
    """Called when the plug-in is unloaded by Nion Swift."""
    api_broker.panel_type_registry.unregister_panel("basic_image_processing_panel")
