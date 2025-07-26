export type params = {
    bankName: paramAxis,
    accountName: paramAxis,
    amount: paramAxis,
    dateTime: paramAxis
} | null

export type paramStatus = {
    bankName: boolean,
    accountName: boolean,
    amount: boolean,
    dateTime: boolean
}

export type sharedParams = {
    status: paramStatus | null;
    file: any;
    areas: params | null;
}

export type paramAxis = {
    xAxis: number|null,
    yAxis: number|null,
    height: number|null,
    width: number|null
}

export type paramValues = {
    bankName: string,
    accountName: string,
    amount: number,
    dateTime: string
}

export type ProcessedPointers = { x: number, y:number, h:number, w:number }