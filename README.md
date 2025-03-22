# Data Structure Visualizer
## General Use
A python library to easily visualize data structures.  
built as a final project for Ort College python course.

## Data Structures
#### The tool can visualize and includes the following data structures:
  - **Lists** (native python lists- not included as a data structure)
  - **Linked List** (works as a Queue)
  - **Binary Tree**
  - **Graph**
  - **Node** (base data structure for Linked Lists, Binary Trees and Graphs)

## Dependencies
  - The visualizer library can only visuzlize native **python lists and included data structures**.
  - This library depends and is built on the python library **pygame**.
 
> [!NOTE]
> When visualizing make sure the visualizing library algorithm is run in some kind of loop or recursion.  
> Alternatively- repeatedly use ```vis.handle_events()``` to avoid unexpected behavior
   
## Example
```python
# Import library's data structures and visualizing functions
from visualizer.data_structures import *
import visualizer as vis

# Initialize display
vis.init() 

# Visualize algorithm or data structure changes using the library functions...

# Terminate display
vis.close()
```
