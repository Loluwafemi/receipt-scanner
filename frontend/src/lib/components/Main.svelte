<script lang="ts">
    import { Fabricating } from "$lib/fiber/extractor";
    import type { paramAxis, params, paramValues, sharedParams } from "$lib/types";
    import { Canvas, FabricImage, Rect } from "fabric";
    export let sharedParam: sharedParams;
    export let axixValues: params;
    export let processedAxis: params;
    export let outputData: paramValues;
    let readyToDraw: boolean = false
    let fileType:string;

    const workingStyle =
        "card-body border-base-content/20 rounded-box flex justify-center items-center";

    let selectedFile: File;
    let fabricObject: Fabricating;

    function dragOver(event: Event) {
        event.preventDefault();
        let canva = document.querySelector(".worksheet")!;
        // canva.classList.toggle("skeleton-striped");
    }

    function dragOff(event: Event) {
        event.preventDefault();
        let canva = document.querySelector(".worksheet")!;
        // canva.classList.toggle("skeleton-striped");
    }

    function OnDrop(event: InputEvent) {
        event.preventDefault();
        if (event?.dataTransfer?.files!) {
            const currentFIle = event.dataTransfer.files[0]
            setImageOnCanava(currentFIle)
        }
    }

    function setImageOnCanava(imageFile:File) {
    const canvas: HTMLCanvasElement = document.querySelector(".fabricCanav")!;
        if (imageFile) {
            const reader = new FileReader();
            reader.addEventListener("load", async (readerEvent) => {
                const image = new Image();
                const currentfileType = readerEvent.target?.result?.toString().split(";")[0].split(":")[1]
                fileType = currentfileType!
                
                image.setAttribute("src", readerEvent.target?.result);
                image.addEventListener("load", () => {
                    fabricObject = new Fabricating(image, canvas);
                });
            });
            reader.readAsDataURL(imageFile);
            readyToDraw = true
            sharedParam.file = imageFile
        }
    }

    function selectFile(event:Event) {
        if (event.target?.files) {
            const currentFIle = event.target.files[0]
            setImageOnCanava(currentFIle)
        }
    }

    async function submitViewPoint(axixValues: params) {
        const resultFromScanner = (await fabricObject.lookupViewPoint(axixValues, fileType))
        processedAxis = resultFromScanner.ProcessparamAxis
        sharedParam.areas = axixValues
        outputData = resultFromScanner.output        
    }

</script>

<div class="flex flex-col h-[100vh] border worksheet">

    <!-- replaceable -->
    <div class="card imagePicker">
        <div class="card-body border-dashed border p-4">
            <div class="card-actions">
                <input on:change={selectFile} class="btn btn-primary" placeholder="Select Receipt" type='file' accept="image/*" multiple={false}/>
            </div>
        </div>
        <button on:click={async ()=> await submitViewPoint(axixValues)} 
            class="bg-primary rounded-lg p-2"
            disabled={!readyToDraw}
            >
            Check View Point 
        </button>
    </div>

    <canvas class="h-screen mb-2 fabricCanav"
    on:dragover={dragOver}
    on:dragleave={dragOff}
    on:drop={OnDrop}
    >

    </canvas>

</div>


