from . import Plugin


class NativeProto2Plugin(Plugin):
    priority = 5
    targets = []

    def upgrade_metric(self, metric):
        if '=' in metric:
            if getattr(self.config, 'process_native_proto2', True):
                nodes = metric.split('.')
                tags = {}
                for (i, node) in enumerate(nodes):
                    if '=' in node:
                        node = node.split('=', 1)
                        tags[node[0]] = node[1]
                    else:
                        tags["n%d" % (i + 1)] = node
                target = {
                    'id': metric,
                    'tags': tags
                }
                return (self.get_target_id(target), target)
            else:
                return False
        return None
# vim: ts=4 et sw=4:
