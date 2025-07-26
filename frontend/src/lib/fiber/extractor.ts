import type { paramAxis, params, paramValues, ProcessedPointers } from '$lib/types';
import { Canvas, FabricImage, Point, Rect, FabricText } from 'fabric';
import type { TPointerEvent, TPointerEventInfo } from 'fabric';

/* 
Aim:
create a function or a class where an image in encaved and a function / method is called whenever there is a selection. the function enables user to select from the list of param as a label for each selection.

*/


//  configure canva outside

export class Fabricating {
    private fabric: Canvas
    private isDrawing: boolean = false
    private rect: Rect
    livePointers: { x: number, y:number, h:number, w:number } = {x: 0, y: 0, h: 0, w: 0}
    constructor(file:HTMLImageElement, canvaElement:HTMLCanvasElement ){
        Canvas.ownDefaults.viewportTransform = [0.42, 0, 0, 0.4, 0, 0]
        Canvas.ownDefaults.height = file.height / 3
        Canvas.ownDefaults.width = file.width / 2


        this.fabric = new Canvas(canvaElement)
        const fabricImg = new FabricImage(file)

        this.fabric.backgroundImage = fabricImg
        this.fabric.renderAll()
        

        // select parameters
        this.fabric.on('mouse:down', (event)=> {
            this.isDrawing = true
            const pointer = event.scenePoint
            this.livePointers.x = pointer.x
            this.livePointers.y = pointer.y

            this.rect = new Rect({
                left: pointer.x,
                top: pointer.y,
                fill: "transparent",
                width: 0,
                height: 0,
                stroke: 'green',
                strokeWidth: 5,
                absolutePositioned: true,
            })

            this.fabric.add(this.rect)
        })


        this.fabric.on("mouse:move", (event)=>{
            if (!this.isDrawing) return;
            const pointer = event.scenePoint
            this.rect.set({
                width: pointer.x - this.rect.left,
                height: pointer.y - this.rect.top
            })
            this.fabric.renderAll()
        })

        this.fabric.on("mouse:up", (event)=>{

            this.livePointers.h = this.rect.height
            this.livePointers.w = this.rect.width

            const rectDimension = JSON.stringify(this.livePointers, null, 3)
            
            const selectedrectDimension = new FabricText(rectDimension, {
                left: this.livePointers.x,
                top: event.scenePoint.y,
                fontSize: 35,
                borderColor: 'yellow',
                stroke: 'blue'
            })

            this.fabric.add(selectedrectDimension)
            this.fabric.renderAll()
            this.isDrawing = false
        })

    }


    lookupViewPoint(axis: params): { status: boolean, output: paramValues, ProcessparamAxis: params}{

        /* 
        This is usable by user and api to get the data on a particular scenepoint. Using the configurations from constructor.
        Steps to converting scenepoint data to string:
        1. iterate through each axis
        2. streamline on every iteration
        3. use output to determine param values approval
        4. draw rectangle on every iteration
        */
        const ProcessedPointers: ProcessedPointers = {x: 0, y: 0, h: 0, w: 0}

        Object.keys(axis).forEach((axisKey)=>{

            if (!axis[axisKey].xAxis || !axis[axisKey].yAxis || !axis[axisKey].height || !axis[axisKey].width) return 

            ProcessedPointers.x = Number(axis[axisKey].xAxis)
            ProcessedPointers.y = Number(axis[axisKey].yAxis)
            ProcessedPointers.h = Number(axis[axisKey].height)
            ProcessedPointers.w = Number(axis[axisKey].width)
            

            this.rect = new Rect({
                left: ProcessedPointers.x,
                top: ProcessedPointers.y,
                fill: "transparent",
                width: ProcessedPointers.w,
                height: ProcessedPointers.h,
                stroke: 'red',
                strokeWidth: 5,
                absolutePositioned: true,
            })


            const positions = JSON.stringify({
                x: ProcessedPointers.x,
                y: ProcessedPointers.y,
                height: ProcessedPointers.h,
                width: ProcessedPointers.w
            }, null, 3)

            
            const selectedPosition = new FabricText(positions, {
                left: ProcessedPointers.x - (ProcessedPointers.x/4),
                top: ProcessedPointers.y,
                fontSize: 35,
                borderColor: 'yellow',
                stroke: 'green'
            })
            this.fabric.add(this.rect, selectedPosition)
            this.fabric.renderAll()

        })


        let ProcessparamAxis:params = axis

        return {
            status: false,
            ProcessparamAxis: ProcessparamAxis,
            output: {
                accountName: '',
                amount: 0,
                bankName: '',
                dateTime: ''
            }
        }
    }


}