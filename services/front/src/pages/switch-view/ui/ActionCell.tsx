import { KTIcon } from "shared"
import { downloadSwitchContent } from "../api/requests"
import fileDownload from "js-file-download";
import { ISwitchDetails } from "entities/switch";
import { StringOptionsWithImporter } from "sass";

type Props = {
  ip: string
  data: ISwitchDetails
  className?: string
}

const ActionCell = ({ ip, data, className } : Props) => {

  const fileName = `${ip} ${data.model} ${data.created_on}.txt`
  
  const download = async () => {
    const result = await downloadSwitchContent(data.id)

    if (result.status === 200) {
      fileDownload(result.data, fileName);
    }
  }
  
  return (
    <>
      <span role={'button'} onClick={download} className="btn btn-light btn-sm">
        <KTIcon iconName="file-down" className="fs-2" />
        Скачать
      </span>
    </>
  )
}

export { ActionCell }
