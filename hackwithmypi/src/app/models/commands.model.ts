export class Commands{
    id: number;
    command: string;
    paramters:  string;
    alreadyExists: boolean;
    argumentsProv: string;
    isPiped: boolean;
    userid: number;
    isAlais: boolean;
    orginal: string;
    pastaComments: boolean;
    isRoot: boolean;

}

export class ServerReply {
    id: number;
    replyText: string;
    alreadyExists: boolean;
    
}