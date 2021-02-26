
# C:\Users\Dan.Edens\Desktop\Tree\the_lab\Python\qv\qv_direct>ptpython
# done
# >>> import nest_asyncio
#... nest_asyncio.apply()

#>>> asyncio.run(main())
#done

import asyncio
import nest_asyncio
import qv_direct.Scanner

# if __package__ is None or __package__ == '':
#     # uses current directory visibility
# else:
#     # uses current package visibility
#     from . import qv_direct.Scanner


async def main():    
    await qv_direct.Scanner.Scan()
    print('done')


def run(_funct=main()):
    asyncio.run(_funct)

 
if __name__ == "__main__":
    nest_asyncio.apply()
    
    
