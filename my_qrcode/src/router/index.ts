import {createRouter,createWebHistory} from 'vue-router'
import Image2code from '@/components/Image2code.vue'
import Text2code from '@/components/Text2code.vue'

const router=createRouter(
    {
        history:createWebHistory(),
        routes:[
            {
                path:"/",
                redirect:"/Iext2code"
            },
            {
                path:"/Iext2code",
                component:Text2code,
                name:'Text'

            },
            {
                path:"/Image2code",
                component:Image2code,
                name:'Image'
            }
        ]
    }
)

export default router