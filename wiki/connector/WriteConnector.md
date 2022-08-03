# A guide on how to develop a connector

## A brief description

Writing connector is the main goal of this project. The modularity is also an important point as ...

## Template of a connector

```python
from connector.AbstractConnector import AbstractConnector


class MyOwnConnector(AbstractConnector):

    def get_optionals_parameters(self) -> list[str]:
        # Not already use
        # If a param of this list is missing, the connector should raise an exception
        pass

    def set_optional_parameter(self, param_name: str, param_value: str):
        pass

    def auth(self, username: str, password: str):
        # Deprecated, behaviour will change in future 
        pass

    def set_instance(self, url: str):
        # Deprecated, use set_optional_parameter instead 
        pass

    def update_dns(self, domain: str, ip: str):
        pass
```

## General description

As you can see, apart `set_instance` and `auth` (who their usage is highly discouraged), you have to, in order:

- Set the *required* parameters (specified by get_optionals_parameters)
- Call `update_dns` with self-explained parameters

As time of writing, only the Mail in a box connector still use `auth` and `set_instance` methods. 