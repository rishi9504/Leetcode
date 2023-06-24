class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path into components
        components = path.split('/')

    # Process each component of the path
        result = []
        for component in components:
        # Ignore empty strings and '.'
            if component == '' or component == '.':
                continue
        # Handle '..'
            elif component == '..':
                if result:
                    result.pop()
        # Add other components
            else:
                result.append(component)

    # Join the components back together
        simplified_path = '/' + '/'.join(result)

        return simplified_path
