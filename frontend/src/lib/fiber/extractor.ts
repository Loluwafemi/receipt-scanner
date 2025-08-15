import type { paramAxis, params, paramValues, ProcessedPointers } from '$lib/types';
import { Canvas, FabricImage, Point, Rect, FabricText } from 'fabric';
import type { TPointerEvent, TPointerEventInfo } from 'fabric';
import { area_of_interest, file_of_interest } from './request';

/* 
Aim:
create a function or a class where an image in encaved and a function / method is called whenever there is a selection. the function enables user to select from the list of param as a label for each selection.

*/


//  configure canva outside

export class Fabricating {
    private fabric: Canvas
    private isDrawing: boolean = false
    private rect: Rect
    private contextFile: FabricImage
    livePointers: { x: number, y:number, h:number, w:number } = {x: 0, y: 0, h: 0, w: 0}
    constructor(file:HTMLImageElement, canvaElement:HTMLCanvasElement ){
        // Canvas.ownDefaults.viewportTransform = [0.42, 0, 0, 0.4, 0, 0]
        Canvas.ownDefaults.height = file.height / 3
        Canvas.ownDefaults.width = file.width / 2
        this.fabric = new Canvas(canvaElement)

        const currentCanvaZoom = this.fabric.getZoom()
        const newZoom = currentCanvaZoom * 0.3
        this.fabric.setZoom(newZoom)

        const fabricImg = new FabricImage(file)
        this.contextFile = fabricImg

        // convert this fabricImage to file Image

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


    async  lookupViewPoint(axis: params, fileType:string ): Promise<{ status: boolean, output: paramValues, ProcessparamAxis: params}>{
        const ProcessedPointers: ProcessedPointers = {x: 0, y: 0, h: 0, w: 0}

        /* 
        This is usable by user and api to get the data on a particular scenepoint. Using the configurations from constructor.
        Steps to converting scenepoint data to string:
        1. iterate through each axis
        2. streamline on every iteration
        3. use output to determine param values approval
        4. draw rectangle on every iteration
        */
    //    const currentFileType = fileType!.split("/")[1]
       const fabricImageBlob = await this.contextFile.toBlob()
       const fileName = `currentFile_${Date.now()}`
       const file: File = new File([fabricImageBlob!], fileName, {
        type: fileType
       })


       const generatedText: paramValues = {
        accountName: '',
        amount: 0,
        bankName: '',
        dateTime: ''
        }
        
        const verifyAreaOfInterest = await file_of_interest({file: file}).then((contentOperation) => {

            if(!contentOperation.status){
                console.log(contentOperation.message);
            }

            Object.entries(axis!).forEach(async (axisKey, index, [])=>{

                const getTextFromFile = await area_of_interest({file: file, coordinate: axisKey[1]})
                
                Object.keys(generatedText).forEach((parameter, indx)=>{

                    if (axisKey[0] === parameter) {
                        generatedText[parameter] = getTextFromFile.content
                    }
                    
                    
                })

                console.log(getTextFromFile);

                if (!axisKey[1].xAxis || !axisKey[1].yAxis || !axisKey[1].height || !axisKey[1].width) return 

                ProcessedPointers.x = Number(axisKey[1].xAxis)
                ProcessedPointers.y = Number(axisKey[1].yAxis)
                ProcessedPointers.h = Number(axisKey[1].height)
                ProcessedPointers.w = Number(axisKey[1].width)
                

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

        })


        let ProcessparamAxis:params = axis

        return {
            status: false,
            ProcessparamAxis: ProcessparamAxis,
            output: generatedText
        }
    }


}