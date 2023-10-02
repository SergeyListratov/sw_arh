import { APP_URL, DataTable, PageTitle, QueryRequestProvider, QueryResponseProvider, SearchComponent, useQueryRequest, useQueryResponse } from "shared";
import { QUERIES, getAll } from "./api/requests";
import { ISwitch } from "entities/switch";
import { useNavigate } from "react-router-dom";
import { dataTableColumns } from "./ui/dataTableColumns";

type Props = {

}

const Grid = () => {
  const request = useQueryRequest()
  const response = useQueryResponse()

  const navigate = useNavigate()

  const click = (data: ISwitch) => navigate(APP_URL.SWITCHES_VIEW(data.ip)) 
  
  return (
    <>
      <PageTitle toolBarActions={<SearchComponent queryRequest={request} size="sm"/>}>Коммутаторы</PageTitle>
      <DataTable queryResponse={response} dataTableColumns={dataTableColumns()} onRowClick={(e) => click(e)} hover={true}/>
    </>
    
  );
};

const SwitchesListPage = ({}: Props) => {
  return (
    <>
      <QueryRequestProvider requestName={QUERIES.GET_ALL}>
        <QueryResponseProvider getRequest={getAll} requestName={QUERIES.GET_ALL}>
          <Grid/>
        </QueryResponseProvider>
      </QueryRequestProvider>
    </>
  );
};

export default SwitchesListPage