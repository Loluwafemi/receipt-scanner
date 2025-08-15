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
    file: File | null;
    areas: params | null;
    output: paramValues | null
}

export type paramAxis = {
    xAxis: number|null,
    yAxis: number|null,
    height: number|null,
    width: number|null
}

export type paramValues = {
    bankName: string | null,
    accountName: string | null,
    amount: number | null,
    dateTime: string | null
}

export type ProcessedPointers = { x: number, y:number, h:number, w:number }